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
    return render_template('rooms.html', rooms=dbRoom)

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

if __name__ == '__main__':
    app.run(debug=True)
