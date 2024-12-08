from django import forms

class create_new_task(forms.Form):
    title = forms.CharField(label="Ttitulo de la tarea: ", max_length=200)
    description = forms.CharField(
        label="Descripcion de la tarea", 
        required=False,
        widget=forms.Textarea
        )
    id_Proyect = forms.IntegerField(label="Id del proyecto al que pertenece")

class create_project(forms.Form):
    name = forms.CharField(label="Nonbre del proyecto: ", max_length=150)
    