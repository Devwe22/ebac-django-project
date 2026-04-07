from django.db import models


class Professor(models.Model):
    """Modelo para representar um professor da EBAC."""
    
    nome = models.CharField(max_length=255, verbose_name="Nome do Professor")
    email = models.EmailField(unique=True, verbose_name="Email")
    especialidade = models.CharField(max_length=255, verbose_name="Especialidade")
    bio = models.TextField(blank=True, verbose_name="Biografia")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Curso(models.Model):
    """Modelo para representar um curso oferecido pela EBAC."""
    
    NIVEL_CHOICES = [
        ('iniciante', 'Iniciante'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    ]
    
    titulo = models.CharField(max_length=255, verbose_name="Título do Curso")
    descricao = models.TextField(verbose_name="Descrição")
    professor = models.ForeignKey(
        Professor,
        on_delete=models.PROTECT,
        related_name='cursos',
        verbose_name="Professor Responsável"
    )
    nivel = models.CharField(
        max_length=20,
        choices=NIVEL_CHOICES,
        default='iniciante',
        verbose_name="Nível"
    )
    duracao_horas = models.IntegerField(verbose_name="Duração em Horas")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(null=True, blank=True, verbose_name="Data de Término")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.titulo


class Aluno(models.Model):
    """Modelo para representar um aluno matriculado em cursos."""
    
    nome = models.CharField(max_length=255, verbose_name="Nome do Aluno")
    email = models.EmailField(unique=True, verbose_name="Email")
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    cursos = models.ManyToManyField(
        Curso,
        related_name='alunos',
        verbose_name="Cursos Inscritos"
    )
    data_inscricao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Inscrição")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
