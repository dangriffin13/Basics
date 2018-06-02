
import collections

result_order = ['Rotich', 'Lilesa','Rupp','Ghebreslassie','Simbu','Ward','Abraham']

marathoners = {'Rotich':'Kenya', 'Lilesa':'Ethiopia', 'Rupp':'USA',
    'Ghebreslassie':'Eritrea','Simbu':'Tanzania','Ward':'USA','Abraham':'Switzerland'}

results_dict = collections.OrderedDict()

for name in result_order:
    results_dict[name] = marathoners[name]




if __name__ == "__main__":
    print("Collections file is running")

    print("Marathoners:")
    print(marathoners)
    print("Marathon results:")
    print([name for names in result_order])
    print("Ordered Dictionary of results:")
    print(results_dict)
