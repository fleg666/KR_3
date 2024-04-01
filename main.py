from functions import *

lst = get_lst()
lst_2 = filter_lst(lst)

print()
print("\n".join(map(print_operation,
                    map(reformat_date,
                        map(mask_kard,
                            map(mask_account,
                                sorted(lst_2, reverse=True, key=lambda x: x["date"])[:5]))))))