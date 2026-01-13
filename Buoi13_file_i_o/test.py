import numpy as np
import matplotlib.pyplot as plt

# Tạo theta
theta = np.linspace(0, 2*np.pi, 2000)

# Hai hàm cực
r1 = np.cos(2*theta)
r2 = np.sin(2*theta)

# Tạo hệ tọa độ cực
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')

# Vẽ đồ thị
ax.plot(theta, r1, label=r'$r=\cos(2\theta)$', linewidth=2)
ax.plot(theta, r2, label=r'$r=\sin(2\theta)$', linewidth=2)

# Trang trí
ax.set_title('Đồ thị trong hệ tọa độ cực', pad=15)
ax.legend(loc='upper right')
ax.grid(True)

plt.show()


