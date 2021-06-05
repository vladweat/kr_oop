import os.path
import pickle

db_folder = 'db'


class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Worker(Person):
    '''Класс Worker хранит информацию о сотруднике'''

    def __init__(self, first_name, last_name, still_working='no info'):
        super(Worker, self).__init__(first_name, last_name)
        self.sys_worker_num = 1
        self.still_working = still_working

    def __call__(self, value):
        self.still_working = value

    def __str__(self):
        return f'Worker {self.first_name + "" + self.last_name} has {self.still_working} status'


class HeadDep(object):
    '''Класс HeadDep хранит информацию о руководителе'''

    def __init__(self, first_name, last_name, status=None, age=None, phone=None):
        self.worker = Worker(first_name, last_name)
        self.status = status
        self.age = age
        self.phone = phone

    def __call__(self, value):
        self.age = value

    def show_info(self):
        print(self.worker.first_name, self.worker.last_name, self.worker.still_working, self.phone, self.age, sep=' : ')


class RespDep(object):
    '''Класс RespDep хранит информацию о материально ответственном лице'''

    def __init__(self, first_name, last_name, status=None, age=None, phone=None):
        self.worker = Worker(first_name, last_name)
        self.status = status
        self.age = age
        self.phone = phone

    def __call__(self, value):
        self.age = value

    def show_info(self):
        print(self.worker.first_name, self.worker.last_name, self.worker.still_working, self.phone, self.age, sep=' : ')


class Tech(object):
    '''Класс RespDep хранит информацию о материально ответственном лице'''

    def __init__(self, inventory_num, name, model, date_of_purchase=None, current_location=None):
        self.sys_tech_num = 1
        self.inventory_num = inventory_num
        self.name = name
        self.model = model
        self.date_of_purchase = date_of_purchase
        self.current_location = current_location

    def show_info(self):
        print(f'Tech inv num: {self.inventory_num}, name: {self.name}, model: {self.model}, '
              f'purchase date: {self.date_of_purchase}, current_location: {self.current_location}')


class Room(object):
    '''Класс Room хранит информацию о помещении, где хранится техника'''

    def __init__(self, room_num, department=None):
        self.sys_room_num = 1
        self.room_num = room_num
        self.department = department

    def __str__(self):
        return self.room_num + ' ' + self.department


class Department(object):
    '''Класс Department хранит информацию о подразделении/департаменте'''

    def __init__(self, department_num, short_name, long_name, head=None, material_resp=None):
        self.sys_department_num = 1
        self.department_num = department_num
        self.short_name = short_name
        self.long_name = long_name
        self.head = head
        self.material_resp = material_resp

    def show_info(self):
        print(self.department_num, self.short_name, self.long_name, self.head, self.material_resp, sep=' : ')


class Transaction(object):
    '''Класс Transaction хранит информацию о перемещении техники'''

    def __init__(self, new_location, old_location, tech, new_resp, date=None):
        self.transaction_num = 1
        self.new_location = new_location
        self.old_location = old_location
        self.tech = tech
        self.new_resp = new_resp
        self.date = date

    def show_info(self):
        print(f'new loc: {self.new_location}, old loc: {self.old_location}, tech inv: {self.tech}, '
              f'new resp: {self.new_resp}, date: {self.date}')


# 8 Лабораторная
class TechDatabase(object):
    def __init__(self):
        self.filename = db_folder + '/' + 'techs.pkl'
        self.database = {}
        self.index = 0
        self.deleted_index = []
        self.deleted_index_filename = db_folder + '/' + 'deleted_indexes_techs.pkl'
        try:
            self.open_database()
        except:
            self.save_database()
            if os.path.exists(self.deleted_index_filename):
                os.remove(self.deleted_index_filename)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_tech(self, inventory_num, name, model, date_of_purchase=None, current_location=None):
        tech = Tech(inventory_num, name, model, date_of_purchase, current_location)
        if len(self.database) != 0:
            if len(self.database) != max(self.database.keys()):
                if os.path.exists(self.deleted_index_filename):
                    with open(self.deleted_index_filename, 'rb') as f:
                        self.deleted_index = pickle.load(f)
                min_index = min(self.deleted_index)
                tech.sys_tech_num = min_index
                self.deleted_index.remove(min_index)
                with open(self.deleted_index_filename, 'wb') as f:
                    pickle.dump(self.deleted_index, f)
                f.closed
        if tech.sys_tech_num in self.database:
            tech.sys_tech_num = len(self.database) + 1
        self.database[tech.sys_tech_num] = tech
        self.database = dict(sorted(self.database.items()))
        self.save_database()

    def get_tech_by_index(self, index):
        if index not in self.database:
            return None
        return self.database[index]

    def delete_tech(self, index):
        if isinstance(index, str):
            index = int(index)
        if index in self.database:
            del self.database[index]
            if os.path.exists(self.deleted_index_filename):
                with open(self.deleted_index_filename, 'rb') as f:
                    self.deleted_index = pickle.load(f)
            self.deleted_index.append(index)
            with open(self.deleted_index_filename, 'wb') as f:
                pickle.dump(self.deleted_index, f)
            f.closed
            self.save_database()

    def change_inventory_number(self, index, num):
        if isinstance(index, str):
            index = int(index)
        tech = self.get_tech_by_index(index)
        if not tech:
            return
        tech.inventory_num = num
        self.save_database()

    def change_name(self, index, name):
        if isinstance(index, str):
            index = int(index)
        tech = self.get_tech_by_index(index)
        if not tech:
            return
        tech.name = name
        self.save_database()

    def change_model(self, index, model):
        if isinstance(index, str):
            index = int(index)
        tech = self.get_tech_by_index(index)
        if not tech:
            return
        tech.model = model
        self.save_database()

    def change_date_of_purchase(self, index, date):
        if isinstance(index, str):
            index = int(index)
        tech = self.get_tech_by_index(index)
        if not tech:
            return
        tech.date_of_purchase = date
        self.save_database()

    def change_current_location(self, index, location):
        if isinstance(index, str):
            index = int(index)
        tech = self.get_tech_by_index(index)
        if not tech:
            return
        tech.current_location = location
        self.save_database()


class RoomDatabase(object):
    def __init__(self):
        self.filename = db_folder + '/' + 'rooms.pkl'
        self.database = {}
        self.index = 0
        self.deleted_index = []
        self.deleted_index_filename = db_folder + '/' + 'deleted_indexes_rooms.pkl'
        try:
            self.open_database()
        except:
            self.save_database()
            if os.path.exists(self.deleted_index_filename):
                os.remove(self.deleted_index_filename)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_room(self, room_num, department):
        room = Room(room_num, department)
        if len(self.database) != 0:
            if len(self.database) != max(self.database.keys()):
                if os.path.exists(self.deleted_index_filename):
                    with open(self.deleted_index_filename, 'rb') as f:
                        self.deleted_index = pickle.load(f)
                min_index = min(self.deleted_index)
                room.sys_room_num = min_index
                self.deleted_index.remove(min_index)
                with open(self.deleted_index_filename, 'wb') as f:
                    pickle.dump(self.deleted_index, f)
                f.closed
        if room.sys_room_num in self.database:
            room.sys_room_num = len(self.database) + 1
        self.database[room.sys_room_num] = room
        self.database = dict(sorted(self.database.items()))
        self.save_database()

    def get_room_by_index(self, index):
        if index not in self.database:
            return None
        return self.database[index]

    def delete_room(self, index):
        if isinstance(index, str):
            index = int(index)
        if index in self.database:
            del self.database[index]
            if os.path.exists(self.deleted_index_filename):
                with open(self.deleted_index_filename, 'rb') as f:
                    self.deleted_index = pickle.load(f)
            self.deleted_index.append(index)
            with open(self.deleted_index_filename, 'wb') as f:
                pickle.dump(self.deleted_index, f)
            f.closed
            self.save_database()

    def change_room_num(self, index, num):
        if isinstance(index, str):
            index = int(index)
        room = self.get_room_by_index(index)
        if not room:
            return
        room.room_num = num
        self.save_database()

    def change_room_department(self, index, department):
        if isinstance(index, str):
            index = int(index)
        room = self.get_room_by_index(index)
        if not room:
            return
        room.department = department
        self.save_database()


class WorkerDepDatabase(object):
    def __init__(self):
        self.filename = db_folder + '/' + 'workers.pkl'
        self.database = {}
        self.index = 0
        self.deleted_index = []
        self.deleted_index_filename = db_folder + '/' + 'deleted_indexes_workers.pkl'
        try:
            self.open_database()
        except:
            self.save_database()
            if os.path.exists(self.deleted_index_filename):
                os.remove(self.deleted_index_filename)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_head_dep(self, first_name, last_name, status=None, age=None, phone=None):
        head_dep = HeadDep(first_name, last_name, status, age, phone)
        if len(self.database) != 0:
            if len(self.database) != max(self.database.keys()):
                if os.path.exists(self.deleted_index_filename):
                    with open(self.deleted_index_filename, 'rb') as f:
                        self.deleted_index = pickle.load(f)
                min_index = min(self.deleted_index)
                head_dep.worker.sys_worker_num = min_index
                self.deleted_index.remove(min_index)
                with open(self.deleted_index_filename, 'wb') as f:
                    pickle.dump(self.deleted_index, f)
                f.closed
        if head_dep.worker.sys_worker_num in self.database:
            head_dep.worker.sys_worker_num = len(self.database) + 1
        self.database[head_dep.worker.sys_worker_num] = head_dep
        self.database = dict(sorted(self.database.items()))
        self.save_database()

    def add_resp_dep(self, first_name, last_name, status=None, age=None, phone=None):
        resp_dep = RespDep(first_name, last_name, status, age, phone)
        if len(self.database) != 0:
            if len(self.database) != max(self.database.keys()):
                if os.path.exists(self.deleted_index_filename):
                    with open(self.deleted_index_filename, 'rb') as f:
                        self.deleted_index = pickle.load(f)
                min_index = min(self.deleted_index)
                resp_dep.worker.sys_worker_num = min_index
                self.deleted_index.remove(min_index)
                with open(self.deleted_index_filename, 'wb') as f:
                    pickle.dump(self.deleted_index, f)
                f.closed
        if resp_dep.worker.sys_worker_num in self.database:
            resp_dep.worker.sys_worker_num = len(self.database) + 1
        self.database[resp_dep.worker.sys_worker_num] = resp_dep
        self.database = dict(sorted(self.database.items()))
        self.save_database()

    def get_worker_by_index(self, index):
        if index not in self.database:
            return None
        return self.database[index]

    def delete_worker(self, index):
        if isinstance(index, str):
            index = int(index)
        if index in self.database:
            del self.database[index]
            if os.path.exists(self.deleted_index_filename):
                with open(self.deleted_index_filename, 'rb') as f:
                    self.deleted_index = pickle.load(f)
            self.deleted_index.append(index)
            with open(self.deleted_index_filename, 'wb') as f:
                pickle.dump(self.deleted_index, f)
            f.closed
            self.save_database()

    def change_first_name(self, index, first_name):
        if isinstance(index, str):
            index = int(index)
        worker = self.get_worker_by_index(index)
        if not worker:
            return
        worker.worker.first_name = first_name
        self.save_database()

    def change_last_name(self, index, last_name):
        if isinstance(index, str):
            index = int(index)
        worker = self.get_worker_by_index(index)
        if not worker:
            return
        worker.worker.last_name = last_name
        self.save_database()

    def change_status(self, index, status):
        if isinstance(index, str):
            index = int(index)
        worker = self.get_worker_by_index(index)
        if not worker:
            return
        worker.status = status
        self.save_database()

    def change_age(self, index, age):
        if isinstance(index, str):
            index = int(index)
        worker = self.get_worker_by_index(index)
        if not worker:
            return
        worker.age = age
        self.save_database()

    def change_phone(self, index, phone):
        if isinstance(index, str):
            index = int(index)
        worker = self.get_worker_by_index(index)
        if not worker:
            return
        worker.phone = phone
        self.save_database()


if __name__ == '__main__':
    head = HeadDep(first_name='Ivan', last_name='Ivanov', age=35, phone='456544')
    resp = RespDep(first_name='Ivan', last_name='Ivanov', phone='456544')
    department = Department(1, 'dep1', 'department1', head.worker.first_name, resp.worker.last_name)

    print(head.__doc__)

    # dbT = TechDatabase()
    # dbT.add_tech('111', 'name1', 'v1', current_location=department)
    # dbT.add_tech('222', 'name2', 'v2', current_location=department)
    # dbT.add_tech('333', 'name3', 'v3', current_location=department)

    # print(dbT)

    # tech = Tech('123112', 'IBM', 'v2', current_location='dep1')
    # department1 = Department(2, 'dep2', 'department2', head.worker.first_name, resp.worker.last_name)
    # transaction = Transaction(department1.short_name, department.short_name, tech.inventory_num, resp.worker.first_name)
    #
    # tech.show_info()
    # head.show_info()
    # resp.show_info()
    # department.show_info()
    # transaction.show_info()
