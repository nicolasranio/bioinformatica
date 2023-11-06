
seq_a = 'MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE'

seq_b = 'MGDIEKGKKIFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAEGFSYTDANKNKGITWGEDTLMEYLENPKKYIPGTKMIFAGIKKKSERVDLIAYLKDATSK'

comparation = ''
for index in range(len(seq_a)):
    comparation+=('-' if seq_a[index]==seq_b[index] else '#')

print("Sequence 1: %s" % (seq_a))
print("Sequence 2: %s" % (seq_b))
print("Diference:  %s" % (comparation))

