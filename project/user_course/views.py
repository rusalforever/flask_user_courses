from flask import render_template, flash, request, session, redirect, url_for
from flask_paginate import Pagination
import json
from . import user_course
from .models import DataBase
from .forms import UserForm


@user_course.route("/search", methods=["POST"])
def users_filter():
    session['per_page'] = request.form['per_page']
    session['search'] = request.form['search']
    return redirect(url_for('user_course.users'))


@user_course.route('/', methods=["GET"])
def users():
    search = session.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = int(session.get('per_page', 10))
    page_users = DataBase().page_users(page, per_page, search);
    user_list = page_users[0]
    page_count = page_users[1][0]
    pagination = Pagination(page=page, per_page=per_page, total=page_count,
                            css_framework='bootstrap4')
    return render_template('users.html',
                           user_list=user_list,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           search=search,
                           active_page='users'
                           )


@user_course.route("/courses", methods=["GET"])
def courses():
    course_list = DataBase().courses_get();
    return render_template('courses.html',
                           active_page='courses', course_list=course_list)


@user_course.route("/create", methods=["GET", "POST"])
def user_create():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        mobile_phone = request.form['mobile_phone']
        status = request.form['status']
        try:
            DataBase().user_create(
                name, email, phone, mobile_phone, status)
            flash('User created successfully', 'success')
        except Exception as e:
            flash(e, 'error')

    return render_template('user_new.html', form=form, active_page='users')


@user_course.route("/delete/<int:user_id>")
def user_delete(user_id):
    DataBase().user_delete(user_id)
    return redirect(url_for('user_course.users'))


@user_course.route("/edit/<int:user_id>", methods=["GET", "POST"])
def user_edit(user_id):
    if request.method == 'GET':
        user = DataBase().user_get(user_id)
        form = UserForm()
        form.name.data = user[0]
        form.name(render_kw={'readonly': True})
        form.email.data = user[1]
        form.phone.data = user[2]
        form.mobile_phone.data = user[3]
        form.status.data = user[4]
        user_courses = DataBase().user_courses_get(user_id)
        user_courses = [user_course[0] for user_course in user_courses]
    else:
        form = UserForm(request.form)
        user_courses = json.loads(request.form['user_courses'])
        if form.validate():
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            mobile_phone = request.form['mobile_phone']
            status = request.form['status']
            try:
                DataBase().user_update(user_id, name, email, phone, mobile_phone, status)
                DataBase().user_courses_update(user_id, user_courses)
                flash('User updated successfully', 'success')
            except Exception as e:
                flash(e, 'error')
    courses = DataBase().courses_get()
    return render_template('user_edit.html',
                           form=form,
                           user_courses=user_courses,
                           courses={course[0]: course[1] for course in courses},
                           user_id=user_id,
                           active_page='users')
