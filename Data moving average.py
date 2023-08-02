import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('files/project_data.csv')

# print(df.head())

df_close = df['<CLOSE>']
# print(df_close)
df_close = np.array(df_close)
# print(df_close)
# print(len(df_close))

move_size = 30

close_mv = []

for i in range(0, len(df_close)-move_size):

	close_move = df_close[i+0:i+move_size]
	close_move_mean = close_move.mean()

	close_mv.append(close_move_mean)

	# print(close_move)
	# print(close_move_mean)


# print(close_mv)
# print(len(close_mv))

plt.plot(df_close)
plt.legend('every day')

plt.plot(close_mv)
plt.legend('each 30 days')

plt.title('FAMELI close price since 2007 until 2022')
plt.show()