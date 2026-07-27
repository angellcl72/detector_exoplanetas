import pandas as pd
import matplotlib.pyplot as plt

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,discoverymethod,disc_year,pl_orbper,pl_rade,pl_bmasse+from+ps&format=csv"

df = pd.read_csv(url)

df_clean = df.dropna(subset=['pl_orbper', 'pl_rade'])

plt.figure(figsize=(8, 6))
plt.scatter(df_clean['pl_orbper'], df_clean['pl_rade'], alpha=0.5, color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Período orbital (días)')
plt.ylabel('Radio del planeta (Radios terrestres)')
plt.title('Relación entre Período Orbital y Radio')
plt.grid(True, which="both", ls="--", alpha=0.5)

plt.savefig('plots/periodo_vs_radio.png')
print("¡Gráfica guardada con éxito en la carpeta plots!")