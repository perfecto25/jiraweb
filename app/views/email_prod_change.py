# Email Prod Change Notice

from flask import render_template, redirect, url_for, flash
from app import app

from app.blocks.email.forms import *


@app.route('/email', methods=['GET', 'POST'])
def email_init():
    ''' email init, get jira details '''

    form = form_email_init()

    if form.validate_on_submit():
        jira_key = form.jira_key.data
        return redirect(url_for('email_prod_change_generate', 
                                jira_key=jira_key))

    return render_template('forms/email_change.html', 
                          form=form, 
                          title='Maestro - get Jira details', 
                          subject='Send Production Email',
                          summary='enter a Jira # to lookup a ticket'
                          )


@app.route('/email/prod/change/generate/<jira_key>', methods=['GET', 'POST'])
def email_prod_change_generate(jira_key):
    ''' email production change notice '''

    form = form_email_prod_change()
    jira_summary = 'zzzzz'

    if form.validate_on_submit():
        # do processing here
        # send email here
        # if ok then:
        return redirect(url_for('success', jira_key=jira_key))
        # else:
        # return redirect(url_for('error'))

    return render_template('forms/email_change.html', 
                            form=form, 
                            title='Maestro - Email Prod Change', 
                            subject='Notice of Production Change', 
                            jira_key=jira_key,
                            jira_summary=jira_summary)


@app.route('/success/<jira_key>', methods=['GET', 'POST'])
def success(jira_key):
    ''' confirm ok '''
    flash('email sent', 'success')
    return render_template('layouts/main.html', 
                            title='Maestro - Success', 
                            jira_key=jira_key)

@app.route('/error/<jira_key>', methods=['GET', 'POST'])
def error(jira_key):
    ''' error processing '''
    flash('got error', 'danger')
    return render_template('layouts/main.html', 
                            title='Maestro - Error', 
                            jira_key=jira_key)