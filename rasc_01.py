#Rascunhos 01 - Brincando com Booleano

#in -> '1'
#var_01 = bool(input('Digite algo: '))
#out -> True

#in -> '0'
#var_01 = bool(input('Digite algo: '))
#out -> True

#in -> *enter*
#var_01 = bool(input('Digite algo: '))
#out -> False

#in -> ' '
#var_01 = bool(input('Digite algo: '))
#out -> True

#var_01 = bool(0)
#out -> False

#var_01 = bool(int(0))
#out -> False

#var_01 = bool(float(0.0))
#out -> False

#var_01 = bool(0.0)
#out -> False

#var_01 = bool('')
#out -> False

#var_01 = bool(' ')
#out -> True

#var_01 = bool(0.0)
#out -> False

#var_01 = bool(0.0000001)
#out -> True

#var_01 = bool(-0.0)
#out -> False

#var_01 = bool('0')
#out -> True

#var_01 = bool('\n')
#out -> True

#var_01 = bool(None)
#out -> False

#var_00 = ()
#var_01 = bool(var_00)
#out -> False

#var_00 = (0)
#var_01 = bool(var_00)
#out -> False

#var_00 = set()
#var_01 = bool(var_00)
#out -> False

#var_00 = list()
#var_01 = bool(var_00)
#out -> False

#var_00 = dict()
#var_01 = bool(var_00)
#out -> False

#var_00 = (0,0)
#var_01 = bool(var_00)
#out -> True

#var_00 = []
#var_01 = bool(var_00)
#out -> False

#var_00 = [0]
#var_01 = bool(var_00)
#out -> True

#var_00 = {}
#var_01 = bool(var_00)
#out -> False

var_00 = {0}
var_01 = bool(var_00)
#out -> True

print(var_01)