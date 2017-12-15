from flask import render_template, make_response
from .. import main
import dataset as ds
from ..form.create_dataset_form import CreateTransDDataSetForm
from utils.flash import *


@main.route('/dataset_manage')
def dataset_manage():
    info_list = ds.get_all_dataset_info_list()
    resp = make_response(render_template('dataset.html', info_list=info_list))
    return resp


@main.route('/dataset_manage/add')
def dataset_add():
    return make_response(render_template('dataset_add.html', creater_list=creater_list()))


@main.route('/dataset_manage/add/<type>', methods=['GET', 'POST'])
def dataset_add_type(type):
    if type == ds.TYPE_TRANS_D:
        form = CreateTransDDataSetForm()

        if form.validate_on_submit():
            name = form.name.data
            start_date = form.start_date.data
            end_date = form.end_date.data
            date_offset = form.date_offset.data
            if start_date < end_date:
                ds.gen_trans_d_dataset(name, start_date, end_date, int(date_offset))
                flash_success("数据集【%s】创建成功" % name)
            else:
                flash_warning("起始日期需小于截止日期")

        return make_response(render_template('dataset_creater/trans_d.html',
                                             creater_list=creater_list(),
                                             form=form))
    return make_response(render_template('dataset_add.html'))


def creater_list():
    return ds.DATASET_CREATER_LIST
