# API REST ICLINICTEST

Esta é uma API desenvolvida utilizando [Django REST framework][djangorest]

----

# Requerimentos

* Python 3.6
* [Requirements.txt][requirements]

# Instalação

* Clone este repositório
* Instale os requerimentos necessários
pip install -r requirements.txt
* Configure o seu banco de dados em na pasta [settings.py][set]
* Pelo terminal, rode "python manage.py runserver"
* Pelo browser, acesse "127.0.0.1:8000/docs/" para a documentação

* "***********" OU "***********"

* Acesse [173.230.150.95/docs/][docs]

----

# Documentação

Esta API representa um sistema de agendamento

* Informações do agendamento:

```python
{
  "data": "aaaa-mm-dd",
  "hora_inicio": "hh:mm:AM",
  "hora_final": "hh:mm:AM",
  "paciente": "string",
  "procedimento": "lista"
}
```
Opções da lista -> 'consulta','retorno', 'horario bloqueado'



Depois de instalado, acesse "127.0.0.1:8000/docs/" `OU` [173.230.150.95/docs/][docs]

Para fins de testes, todas as permissões dos usuários estão liberadas


[requirements]:https://github.com/bussola/iclinic_teste/blob/master/requirements.txt
[djangorest]:https://github.com/encode/django-rest-framework
[docs]:http://173.230.150.95/docs/
[set]:https://github.com/bussola/iclinic_teste/blob/master/iclinicproject/iclinicproject/settings.py#L80