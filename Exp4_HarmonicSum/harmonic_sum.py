import numpy as np
import matplotlib.pyplot as plt

# ------------------------ 原代码中的函数（保持不变） ------------------------
def sum_up(N):
    """从小到大计算调和级数和：H_N = 1 + 1/2 + ... + 1/N"""
    result = 0.0
    for n in range(1, N + 1):
        result += 1.0 / n
    return result

def sum_down(N):
    """从大到小计算调和级数和：H_N = 1/N + ... + 1/2 + 1"""
    result = 0.0
    for n in range(N, 0, -1):
        result += 1.0 / n
    return result

def calculate_relative_difference(N):
    """计算两种方法的相对差异"""
    s_up = sum_up(N)
    s_down = sum_down(N)
    return abs(s_up - s_down) / abs((s_up + s_down) / 2.0) if (s_up + s_down) != 0 else 0.0

def plot_differences():
    """绘制相对差异随N的变化"""
    N_values = np.logspace(1, 4, 50, dtype=int)
    differences = [calculate_relative_difference(N) for N in N_values]
    
    plt.figure(figsize=(10, 6))
    plt.loglog(N_values, differences, 'o-', alpha=0.7)
    
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.xlabel('N')
    plt.ylabel('Relative Difference')
    plt.title('Relative Difference vs N')
    
    plt.savefig('harmonic_sum_differences.png', dpi=300, bbox_inches='tight')
    plt.show()

def print_results():
    """打印典型N值的计算结果"""
    N_values = [10, 100, 1000, 10000]
    
    print("\n计算结果:")
    print("N\tS_up\t\t\tS_down\t\t\t相对差异")
    print("-" * 80)
    
    for N in N_values:
        s_up = sum_up(N)
        s_down = sum_down(N)
        diff = calculate_relative_difference(N)
        print(f"{N}\t{s_up:.12f}\t{s_down:.12f}\t{diff:.8e}")

def main():
    """主函数"""
    print_results()
    plot_differences()

if __name__ == "__main__":
    main()
