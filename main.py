def nums_input():
    numeros = [0] * 9
    nums = input('nums: ')

    # -Length-
    if len(nums) != 9:
        difference = 9 - len(nums)
        if difference < 0:
            nums = nums[:difference]
        else:
            nums += '0' * difference
    # -Repetition-
    for n in nums:
        if n != '0':
            numeros[int(n)-1] += 1
            if numeros[int(n)-1] >= 2:
                print('Error: Doble Number')
                return 'error'
    return nums


def creat_matriz():
    m = []
    while len(m) < 9:
        fila = []
        nums = nums_input()
        if nums != 'error':
            for n in nums:
                fila.append(n)
            m.append(fila)
    for i in m:
        print(i)


def principal():
    print('yes')
    op = int(input('Ingrese accion:'))
    if op == int(1):
        creat_matriz()


if __name__ == '__main__':
    principal()
