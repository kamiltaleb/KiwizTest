from flask import Blueprint, request, jsonify
import pandas as pd
from flasgger import swag_from
import re

#Permet de créer un point d'entrée pour les routes
bp = Blueprint('routes', __name__)

#Création d'un dataframe vide
data = pd.DataFrame(columns=['Date', 'Type', 'Amount($)', 'Memo'])

#POST pour creer la transaction 
@bp.route('/transactions', methods=['POST'])
@swag_from('swagger/transactions.yml')  
#Fonction qui permet de lire le fichier csv et de le convertir en dataframe
def transactions():
    csv_file = request.files['file']
    print(csv_file.filename)
    global data
    
    # lire le fichier csv et le convertir en dataframe
    csv_content = csv_file.read().decode('utf-8').splitlines()
    
    # on supprime les lignes vides et les lignes qui commencent par #
    processed_lines = [re.split(r',\s*', line) for line in csv_content if line.strip() and not line.startswith('#')]

    
    # on crée un dataframe avec les colonnes Date, Type, Amount($), Memo
    column_names = ['Date', 'Type', 'Amount($)', 'Memo']
    data = pd.DataFrame(processed_lines, columns=column_names)

    # on convertit la colonne Amount($) en float
    data['Amount($)'] = pd.to_numeric(data['Amount($)'])
    
    # on convertit la colonne Date en datetime
    return jsonify(status="success", message="Data uploaded successfully"), 200



@bp.route('/report', methods=['GET'])
@swag_from('swagger/report.yml')
def report():
    # on calcule le revenu brut, les dépenses et le revenu net
    gross_revenue = data[data['Type'] == 'Income']['Amount($)'].sum()
    expenses = data[data['Type'] == 'Expense']['Amount($)'].sum()
    net_revenue = gross_revenue - expenses

    # on retourne le rapport
    report_data = {
        "gross-revenue": gross_revenue,
        "expenses": expenses,
        "net-revenue": net_revenue
    }
    return jsonify(report_data), 200
