from flask import *
from base import app

from base.com.dao.city_dao import CityDAO
from base.com.vo.city_vo import CityVO
from base.com.dao.state_dao import StateDAO


@app.route('/admin/load_city', methods=['get'])
def admin_load_city():
    try:
        state_dao = StateDAO()
        state_vo_list = state_dao.view_state()
        return render_template('admin/addCity.html', state_vo_list=state_vo_list)

    except Exception as ex:
        print('admin_view_city route exception occured>>>>>>>>>>', ex)
        
        
@app.route('/admin/insert_city',methods=['post'])
def admin_add_city():
    try:
        city_vo = CityVO()
        city_dao = CityDAO()

        city_vo.city_name = request.form.get('city_name')
        city_vo.city_description = request.form.get('city_description')
        city_vo.city_state_id = request.form.get('state_id')

        city_dao.insert_city(city_vo)
        return redirect(url_for('admin_view_city'))

    except Exception as ex:
        print("admin_insert_city route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_city', methods=['get'])
def admin_view_city():
    try:
        city_dao = CityDAO()
        city_vo_list = city_dao.view_city()
        return render_template('admin/viewCity.html', city_vo_list=city_vo_list)

    except Exception as ex:
        print("admin_view_city route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_city', methods=['get'])
def admin_delete_city():
    try:
        city_dao = CityDAO()
        city_id = request.args.get('city_id')
        city_dao.delete_city(city_id)
        return redirect(url_for('admin_view_city'))
    except Exception as ex:
        print("in admin_delete_city route exception occured>>>>>>>>>>", ex)
        

@app.route('/admin/edit_city', methods=['get'])
def admin_edit_city():
    try:
        city_vo = CityVO()
        city_dao = CityDAO()
        state_dao = StateDAO()

        city_vo.city_id = request.args.get('city_id')
        city_vo_list = city_dao.edit_city(city_vo)
        state_vo_list = state_dao.view_state()
        return render_template('admin/editCity.html', state_vo_list=state_vo_list,
                               city_vo_list=city_vo_list)
    except Exception as ex:
        print("in admin_edit_city route exception occured>>>>>>>>>>", ex)
        
        
@app.route('/admin/update_city', methods=['POST'])
def admin_update_city():
    try:
        city_vo = CityVO()
        city_dao = CityDAO()

        city_vo.city_id = request.form.get('city_id')
        city_vo.city_name = request.form.get('city_name')
        city_vo.city_description = request.form.get('city_description')
        city_vo.city_state_id = request.form.get('city_state_id')
        city_dao.update_city(city_vo)
        return redirect(url_for('admin_view_city'))
    except Exception as ex:
        print("in admin_update_city route exception occured>>>>>>>>>>", ex)