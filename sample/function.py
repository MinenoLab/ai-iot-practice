def function_a(): # パラメータなし 
        print("function a") 

def function_b(something): # パラメータをsomethingとして使う 
        print(something) 

def print_name(name="nanashi"): # デフォルトのパラメータを設定 
        print("私は" + name + "です") 

function_a() 
function_b("hoge") 
function_b("huga") 
print_name()                # パラメータなしで呼び出し 
print_name(name="Mineno")   # パラメータに"Mineno"を渡して呼び出し 
print_name(name="Ban")      # パラメータに"Ban"を渡して呼び出し 
