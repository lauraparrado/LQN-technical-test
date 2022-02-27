def generic_model_mutation_process(model, data, id=None, commit=True):
    """ Es posible actualizar la instancia de un modelo
     o crearla. Pero esta es cargada a la base de datos
     solo si commit es verdadero si no, solo se retorna esta
     """
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item
