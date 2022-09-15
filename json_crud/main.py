from crud import (
    get_all_data, 
    create_data, 
    get_data_by_id,
    delete_data,
    update
)



if __name__ == '__main__':
    print(get_all_data())
    create_data()
    print(get_data_by_id())
    delete_data()
    update()


# TODO: исправить ошибку с обновлением цены
# TODO: добавить интерфейс
# TODO: обработать момент с несуществующим id