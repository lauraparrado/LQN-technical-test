from io import StringIO

from django.core.management import call_command
from django.views.generic import FormView

from .forms import ExecuteLogicExerciseForm


class ExecuteLogicExerciseView(FormView):
    template_name = "logic_exercise_view.html"
    form_class = ExecuteLogicExerciseForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = form.cleaned_data
            exercise = data.get("exercise")
            out = StringIO()
            call_command(exercise, stdout=out)
            result = out.getvalue()
            return self.render_to_response(
                {
                    "form": self.get_form_class()(
                        initial={"result": result, "exercise": exercise}
                    )
                }
            )
        return self.form_invalid(form)
