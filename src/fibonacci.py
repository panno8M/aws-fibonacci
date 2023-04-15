"""フィボナッチ数列
"""
def fib(n):
    """フィボナッチ数列を求める

    Args:
        n (int): 数列の項数

    Returns:
        int: フィボナッチ数列のn番目の値

    Raises:
        ValueError: 引数nが１以上の整数でない場合に発生
    """
    try:
        n = int(n)
    except ValueError:
        raise ValueError(f"n must be more than 0 but got {n}.")

    if n <= 0:
        raise ValueError(f"n must be more than 0 but got {n}.")
    if n == 1 or n == 2: return 1

    a, b = 1, 1
    for i in range(n-2):
        a, b = b, a+b
    return b
