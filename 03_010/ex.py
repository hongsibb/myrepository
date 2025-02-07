# 파이썬 내장 진수 변환

'''
10진수 -> 2진수, 8진수, 16진수
binary: bin()
octal: oct()
hexadecimal: hex()

반환 결과는 문자열
'''

inputNumber = int(input('10진수 입력'))
print('2진수: {}'.format(bin(inputNumber)))
print('8진수: {}'.format(oct(inputNumber)))
print('16진수: {}'.format(hex(inputNumber)))


#format함수 이용하기
print('2진수: {}'.format(format(inputNumber, '#b')))
print('8진수: {}'.format(format(inputNumber, '#o')))
print('16진수: {}'.format(format(inputNumber, '#x')))

# 앞에 0x 0o 0b.. 진수 상징 없애기
print('2진수: {}'.format(format(inputNumber, 'b')))
print('8진수: {}'.format(format(inputNumber, 'o')))
print('16진수: {}'.format(format(inputNumber, 'x')))


print('{0:#b}{0:#o}{0:#x}'.format(inputNumber))



# x진수를 10진수로 변환

print('2진수(0b11110) -> 10진수({})'.format(int('0b11110',2))) # format 뒤에는 진수와 형태가 들어간다.
print('8진수(Oo36) -> 10진수({})'.format(int('0o36',8))) 
print('2진수(0x1e) -> 10진수({})'.format(int('0x1e',16)))