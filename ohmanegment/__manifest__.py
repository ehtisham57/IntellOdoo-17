{
    'name': 'Management System',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': 'Ehtisham',
    'category': 'Tools',
    'summary': 'Simple management system to store data',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/teacher_views.xml',
        'views/student_views.xml',
        'views/subject.xml',
        'views/menu.xml',
        'wizard/Student_fee_update_wizard_view.xml'

    ],
    'installable': True,
    'application': True,
}
