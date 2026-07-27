import lightkurve as lk
import matplotlib.pyplot as plt
import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np

print("1. Conectando con los datos de la NASA/Kepler...")
# Buscamos las observaciones de la estrella Kepler-8
search = lk.search_lightcurve("Kepler-8", author="Kepler", quarter=1)
print("Archivo de luz encontrado")

print("2. Descargando la curva de luz...")
lc = search.download()

print("3. Limpiando la señal y quitando puntos nulos...")
# Quitamos valores nulos y normalizamos el brillo
clean_lc = lc.remove_nans().normalize()

print("4. Generando gráfica de la luz de la estrella...")
# Dibujamos los datos de brillo respecto al tiempo
ax = clean_lc.plot(title="Curva de Luz de Kepler-8")
plt.show()

print("5. Calculando el período del tránsito del exoplaneta (BLS)...")
# El algoritmo BLS busca patrones periódicos en las caídas de luz
periodogram = clean_lc.to_periodogram(method="bls", period=np.linspace(1, 10, 10000))

# Extraemos el período detectado
planet_period = periodogram.period_at_max_power
print(f"--> ¡EXOPLANETA DETECTADO! Período orbital estimado: {planet_period:.4f}")

print("6. Plegando la luz según el período detectado...")
# Doblamos la gráfica en función del período para ver la "bajada" limpia de luz
folded_lc = clean_lc.fold(period=planet_period)
folded_lc.plot(title=f"Tránsito del Exoplaneta Kepler-8b (Período: {planet_period:.3f})")
plt.show()