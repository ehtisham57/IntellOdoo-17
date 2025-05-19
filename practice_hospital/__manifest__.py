{
    'name': 'hospital pactice',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': 'practice',
    'category': 'Tools',
    'summary': 'Simple practice project',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/specialization_doctor.xml',
        'views/doctor_views.xml',
        'views/patient_appointment.xml',
        'views/menu.xml',

    ],
    'installable': True,
    'application': True,
}
