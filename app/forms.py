from django import forms


class ExecuteLogicExerciseForm(forms.Form):
    exercise = forms.ChoiceField(
        choices=(
            ("logic_exercise_1", "Ejercicio Multiplos"),
            ("logic_exercise_2", "Ejercicio Pokemons"),
        ),
        label="Ejercicio a ejecutar:",
    )
    result = forms.CharField(
        widget=forms.Textarea,
        label="Resultado del ejercicio",
        disabled=True,
        required=False,
    )
