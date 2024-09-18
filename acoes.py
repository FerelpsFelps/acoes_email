# Importa as bibliotecas a serem utilizadas
import yfinance as yf
from datetime import datetime
from matplotlib import pyplot as plt

# Define a data final que será utilizada no Ticker
end_data = datetime.now().strftime('%Y-%m-%d') # Pega a data do atual momento e formata-a para ano-mes-dia

# Define o Ticker da IBOVESPA
ibvsp = yf.Ticker('^BVSP')
data_ibvsp = ibvsp.history(
    start = '2021-09-18',
    end = end_data
)

# Cria o gráfico da ação
data_ibvsp['Close'].plot()
plt.savefig('ibvsp_price.png')

