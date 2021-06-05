from flask import Flask, render_template, url_for, redirect, request
from classes import *

app = Flask(__name__)
dbTech = TechDatabase()


@app.route('/', methods=['GET'])
def index():
    dbTech = TechDatabase()
    return render_template('index.html', techs=dbTech)


@app.route('/techs', methods=['GET'])
def techs_page():
    dbTech = TechDatabase()
    dbRoom = RoomDatabase()
    return render_template('techs.html', techs=dbTech, rooms=dbRoom)


@app.route('/add_tech', methods=['POST'])
def add_tech():
    dbTech = TechDatabase()
    dbRoom = RoomDatabase()
    if request.form['btn'] == 'Add':
        if request.form['add_inp_inventory_num'] != '' and request.form['add_inp_name'] != '' and request.form[
            'add_inp_model'] != '':
            t_inv_num = request.form['add_inp_inventory_num']
            t_name = request.form['add_inp_name']
            t_model = request.form['add_inp_model']
            t_purchase_date = request.form['add_inp_date']
            t_location = request.form['add_inp_location']
            dbTech.add_tech(t_inv_num, t_name, t_model, t_purchase_date, t_location)

    if request.form["btn"] == "Change":

        index = request.form['chg_inp_id']
        chg_inv_num = request.form['chg_inp_inv_num']
        chg_name = request.form['chg_inp_name']
        chg_model = request.form['chg_inp_model']
        chg_date = request.form['chg_inp_date']
        chg_location = request.form['chg_inp_location']

        if index != '' and (index.isdigit()):
            if chg_inv_num != '':
                dbTech.change_inventory_number(index, chg_inv_num)
            if chg_name != '':
                dbTech.change_name(index, chg_name)
            if chg_model != '':
                dbTech.change_inventory_number(index, chg_model)
            if chg_date != '':
                dbTech.change_inventory_number(index, chg_date)
            if chg_location != '':
                dbTech.change_inventory_number(index, chg_location)

    if request.form['btn'] == 'Delete':
        if (request.form['chg_inp_id'] != '') and (request.form['chg_inp_id'].isdigit()):
            dbTech.delete_tech(request.form['chg_inp_id'])
    return redirect(url_for('techs_page'))


@app.route('/rooms', methods=['GET'])
def rooms_page():
    dbRoom = RoomDatabase()
    dbDepartment = DepartmentDatabase()
    return render_template('rooms.html', rooms=dbRoom, departments=dbDepartment)


@app.route('/add_room', methods=['POST'])
def add_room():
    dbRoom = RoomDatabase()

    if request.form['btn'] == 'Add':
        a_room_num = request.form['a_room_num']
        a_department = request.form['a_department']

        if a_room_num != '':
            dbRoom.add_room(a_room_num, a_department)

    if request.form["btn"] == "Change":
        index = request.form['c_sys_room_num']
        c_room_num = request.form['c_room_num']
        c_department = request.form['c_department']

        if index != '' and index.isdigit():
            if c_room_num != '':
                dbRoom.change_room_num(index, c_room_num)
            if c_department != '':
                dbRoom.change_room_num(index, c_department)

    if request.form['btn'] == 'Delete':
        index = request.form['c_sys_room_num']
        if index != '' and index.isdigit():
            dbRoom.delete_room(index)
    return redirect(url_for('rooms_page'))


@app.route('/workers', methods=['GET'])
def workers_page():
    dbWorker = WorkerDepDatabase()
    return render_template('workers.html', workers=dbWorker)


@app.route('/add_worker', methods=['POST'])
def add_worker():
    dbWorker = WorkerDepDatabase()
    if request.form["btn"] == "Add":
        a_first_name = request.form['a_first_name']
        a_last_name = request.form['a_last_name']
        a_status = request.form['a_status']
        a_age = request.form['a_age']
        a_phone = request.form['a_phone']
        if a_first_name != '' and a_last_name != '' and a_status != '':
            if a_status == 'Head':
                dbWorker.add_head_dep(a_first_name, a_last_name, a_status, a_age, a_phone)

            if a_status == 'Resp':
                dbWorker.add_resp_dep(a_first_name, a_last_name, a_status, a_age, a_phone)

    if request.form["btn"] == "Change":
        index = request.form['c_worker_num']
        c_first_name = request.form['c_first_name']
        c_last_name = request.form['c_last_name']
        c_status = request.form['c_status']
        c_age = request.form['c_age']
        c_phone = request.form['c_phone']

        if index != '' and index.isdigit():
            if c_first_name != '':
                dbWorker.change_first_name(index, c_first_name)
            if c_last_name != '':
                dbWorker.change_last_name(index, c_last_name)
            if c_status != '':
                dbWorker.change_status(index, c_status)
            if c_age != '':
                dbWorker.change_age(index, c_age)
            if c_phone != '':
                dbWorker.change_age(index, c_phone)

    if request.form["btn"] == "Delete":
        index = request.form['c_worker_num']
        if index != '' and index.isdigit():
            dbWorker.delete_worker(index)
    return redirect(url_for('workers_page'))


@app.route('/departments', methods=['GET'])
def departments_page():
    dbDepartment = DepartmentDatabase()
    dbWorker = WorkerDepDatabase()
    return render_template('departments.html', departments=dbDepartment, workers=dbWorker)


@app.route('/add_department', methods=['POST'])
def add_department():
    dbDepartment = DepartmentDatabase()
    if request.form["btn"] == "Add":
        a_department_num = request.form['a_department_num']
        a_short_name = request.form['a_short_name']
        a_long_name = request.form['a_long_name']
        a_head = request.form['a_head']
        a_resp = request.form['a_resp']
        if a_department_num != '' and a_short_name != '' and a_long_name != '':
            dbDepartment.add_department(a_department_num, a_short_name, a_long_name, a_head, a_resp)

    if request.form["btn"] == "Change":
        index = request.form['c_index']
        c_department_num = request.form['c_department_num']
        c_short_name = request.form['c_short_name']
        c_long_name = request.form['c_long_name']
        c_head = request.form['c_head']
        c_resp = request.form['c_resp']

        if index != '' and (index.isdigit()):
            if c_department_num != '':
                dbDepartment.change_department_num(index, c_department_num)
            if c_short_name != '':
                dbDepartment.change_short_name(index, c_short_name)
            if c_long_name != '':
                dbDepartment.change_long_name(index, c_long_name)
            if c_head != '':
                dbDepartment.change_head(index, c_head)
            if c_resp != '':
                dbDepartment.change_material_resp(index, c_resp)

    if request.form["btn"] == "Delete":
        index = request.form['c_index']
        if index != '' and index.isdigit():
            dbDepartment.delete_department(index)
    return redirect(url_for('departments_page'))

@app.route('/transactions', methods=['GET'])
def transactions_page():
    dbTransaction = TransactionDatabase()
    dbDepartment = DepartmentDatabase()
    dbWorkers = WorkerDepDatabase()
    dbTech = TechDatabase()
    return render_template('transactions.html', transatcions=dbTransaction, departments=dbDepartment, workers=dbWorkers, techs=dbTech)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    dbTransaction = TransactionDatabase()
    if request.form["btn"] == "Add":
        a_new_location = request.form['a_new_location']
        a_old_location = request.form['a_old_location']
        a_tech = request.form['a_tech']
        a_resp = request.form['a_resp']
        a_date = request.form['a_date']
        dbTransaction.add_transactions(a_new_location, a_old_location, a_tech, a_resp, a_date)

    if request.form["btn"] == "Change":
        index = request.form['c_index']
        c_new_location = request.form['c_new_location']
        c_old_location = request.form['c_old_location']
        c_tech = request.form['c_tech']
        c_resp = request.form['c_resp']
        c_date = request.form['c_date']

        if index != '' and (index.isdigit()):
            if c_new_location != '':
                dbTransaction.change_new_location(index, c_new_location)
            if c_old_location != '':
                dbTransaction.change_old_location(index, c_old_location)
            if c_tech != '':
                dbTransaction.change_tech(index, c_tech)
            if c_resp != '':
                dbTransaction.change_new_resp(index, c_resp)
            if c_date != '':
                dbTransaction.change_date(index, c_date)

    if request.form["btn"] == "Delete":
        index = request.form['c_index']
        if index != '' and index.isdigit():
            dbTransaction.delete_transaction(index)
    return redirect(url_for('transactions_page'))


if __name__ == '__main__':
    app.run(debug=True)
