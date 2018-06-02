
import collections

result_order = ['Rotich', 'Lilesa','Rupp','Ghebreslassie','Simbu','Ward','Abraham']

marathoners = {'Ghebreslassie':'Eritrea','Simbu':'Tanzania','Rotich':'Kenya',
    'Rupp':'USA','Ward':'USA', 'Lilesa':'Ethiopia','Abraham':'Switzerland'}

results_dict = collections.OrderedDict()

for name in result_order:
    results_dict[name] = marathoners[name]




if __name__ == "__main__":
    print("Collections file is running")

    print("Marathoners:")
    print(marathoners)
    print("Marathon results:")
    print(result_order)
    print("Ordered Dictionary of results:")
    print(results_dict)
