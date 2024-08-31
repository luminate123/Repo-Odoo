# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    credits = fields.Integer(string='Credits')
    max_students = fields.Integer(string='Max Students')
    active = fields.Boolean(string='Active', default=True)
    student_ids = fields.Many2many('school.student', string='Students')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')

    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                today = fields.Date.today()
                student.age = today.year - student.birth_date.year - ((today.month, today.day) < (student.birth_date.month, student.birth_date.day))


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    profile = fields.Text(string='Profile')
    subject_ids = fields.One2many('school.subject', 'teacher_id', string='Subjects')
