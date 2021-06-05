from classes import *
import unittest


# class TestChangeINvNumber(unittest.TestCase):
#
#     def setUp(self):
#         self.dbT = TechDatabase()
#         # self.room = Room(15)
#         # self.dbT.add_tech('111', 'name1', 'v1', current_location=self.room.room_num)
#         # self.dbT.add_tech('222', 'name2', 'v2', current_location='department2')
#         # self.dbT.add_tech('333', 'name3', 'v3', current_location='department3')
#
#     def test_add_tech(self):
#         for i in self.dbT:
#             print(i.inventory_num, i.name, i.model, i.current_location)
#         # self.dbT.delete_tech(2)
#         # for i in self.dbT:
#         #     print(i.inventory_num, i.name, i.model, i.current_location)

# class TestAddTechInRoomList(unittest.TestCase):
#
#     def setUp(self):
#         self.dbR = RoomDatabase()
#         self.dbR.add_room(101, 'dep1')
#
#     def test_add_tech(self):
#         for r in self.dbR:
#             print(r.sys_room_num, r.room_num, r.department, r.list_of_tech)
#         self.dbR.add_tech_in_list(1, '10013abc', 'tech name 1', 'model v1')
#         self.dbR.add_tech_in_list(1, 'another', 'tech name 2', 'model v2')
#         self.dbR.add_tech_in_list(1, 'theasd', 'tech name 3', 'model v3')
#         print('-------------')
#         for r in self.dbR:
#             print(r.sys_room_num, r.room_num, r.department, r.list_of_tech)
#         self.dbR.delete_tech_from_list(1, 2)
#         print('-------------')
#         for r in self.dbR:
#             print(r.sys_room_num, r.room_num, r.department, r.list_of_tech)

class TestAddWorker(unittest.TestCase):

    def setUp(self):
        self.dbW = WorkerDepDatabase()
        self.dbW.add_head_dep('ivan', 'ivanovixh', 'Head')
        self.dbW.add_head_dep('ivan', 'ivanovixh', 'Resp')

    def test_add_workers(self):
        for w in self.dbW:
            print(w.worker.sys_worker_num, w.worker.first_name, w.worker.last_name, w.status, w.age, w.phone)

        # self.dbW.change_first_name(1, 'Andrey')
        # self.dbW.delete_worker(2)
        for w in self.dbW:
            print(w.worker.sys_worker_num, w.worker.first_name, w.worker.last_name, w.status, w.age, w.phone)


if __name__ == '__main__':
    unittest.main()
