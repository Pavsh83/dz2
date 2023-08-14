import subprocess
import zlib

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def calculate_crc32(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        crc32_hash = zlib.crc32(data)
        return crc32_hash

falderin = '/home/user/tst'
falderout = '/home/user/out'

def test_step1():
    assert checkout(f'cd {falderin}; 7z a {falderout}/arh1', 'Everything is Ok'), 'test1 FAIL'

def test_step2():
    assert checkout(f'cd {falderin}; 7z u {falderout}/arh1', 'Everything is OK'), 'test2 FAIL'

def test_step3():
    assert checkout(f'cd {falderin}; 7z d {falderout}/arh1', 'Everything is Ok'), 'test3 FAIL'

def test_step4():
    assert checkout(f'cd {falderin}; 7z l {falderout}/arh1', 'Everything is Ok'), 'test4 FAIL'

def test_step5():
    assert checkout(f'cd {falderout}; 7z x {falderout}/arh1', 'Everything is Ok'), 'test5 FAIL'

def test_step6():
    original_file = f'{falderin}/file.txt'
    archived_file = f'{falderout}/arh1/file.txt'
    
    original_crc32 = calculate_crc32(original_file)
    archived_crc32 = checkout(f'7z h {archived_file}', 'CRC32 = ')[-9:].strip()

    assert original_crc32 == int(archived_crc32, 16), 'test6 FAIL'

if __name__ == '__main__':
    test_step1()
    test_step2()
    test_step3()
    test_step4()
    test_step5()
    test_step6()
