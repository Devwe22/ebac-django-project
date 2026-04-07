from django.contrib import admin
from .models import Professor, Curso, Aluno


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'especialidade', 'ativo', 'data_criacao')
    list_filter = ('ativo', 'data_criacao', 'especialidade')
    search_fields = ('nome', 'email', 'especialidade')
    readonly_fields = ('data_criacao',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'especialidade')
        }),
        ('Detalhes', {
            'fields': ('bio', 'ativo')
        }),
        ('Datas', {
            'fields': ('data_criacao',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'professor', 'nivel', 'duracao_horas', 'data_inicio', 'ativo')
    list_filter = ('nivel', 'ativo', 'data_inicio', 'professor')
    search_fields = ('titulo', 'descricao', 'professor__nome')
    readonly_fields = ('data_criacao',)
    fieldsets = (
        ('Informações do Curso', {
            'fields': ('titulo', 'descricao', 'professor')
        }),
        ('Detalhes', {
            'fields': ('nivel', 'duracao_horas', 'ativo')
        }),
        ('Datas', {
            'fields': ('data_inicio', 'data_fim', 'data_criacao')
        }),
    )


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_inscricao', 'ativo')
    list_filter = ('ativo', 'data_inscricao', 'cursos')
    search_fields = ('nome', 'email')
    readonly_fields = ('data_inscricao',)
    filter_horizontal = ('cursos',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'data_nascimento')
        }),
        ('Inscrições', {
            'fields': ('cursos', 'ativo')
        }),
        ('Datas', {
            'fields': ('data_inscricao',),
            'classes': ('collapse',)
        }),
    )
