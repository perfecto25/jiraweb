# Email Prod Change Notice

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

    if form.validate_on_submit():
        flash('its created created!', 'warning')
        return redirect(url_for('email_prod_change_generate', msg='emailed'))

    return render_template('forms/email_change.html', 
                            form=form, 
                            title='Maestro - Email Prod Change', 
                            subject='Notice of Production Change', 
                            jira_key=jira_key)