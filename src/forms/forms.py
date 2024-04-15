from wtforms import Form, FormField, FieldList
from wtforms import (
    StringField,
    TextAreaField,
    IntegerField,
    SelectField,
    RadioField,
    BooleanField,
    PasswordField,
    DateField,
    FloatField,
)
from wtforms import EmailField, HiddenField
from wtforms import validators
from datetime import date


class SignupForm(Form):
    nombre = StringField(
        "nombre",
        [
            validators.DataRequired(message="el campo es requerido"),
            validators.Length(min=4, max=10, message="ingresa nombre valido"),
        ],
    )
    contrasenia = PasswordField(
        "Contraseña",
        [
            validators.DataRequired(message="el campo es requerido"),
            validators.EqualTo("confirmacion", message="las contraseñas no coinciden"),
        ],
    )
    confirmacion = PasswordField("Confirmar Contraseña")
    correo = StringField(
        "Correo",
        [
            validators.DataRequired(message="el campo es requerido"),
            validators.Email(message="ingresa un correo electrónico válido"),
        ],
    )


class SolicitudProduccionForm(Form):

    receta = SelectField(
        "Receta", [validators.DataRequired(message="Selecciona una receta")], choices=[]
    )
    tandas = IntegerField(
        "Número de Tandas",
        [
            validators.DataRequired(message="Ingresa el número de tandas"),
            validators.NumberRange(
                min=1, message="El número de tandas debe ser mayor a 0"
            ),
        ],
    )
    fecha_solicitud = DateField(
        "Fecha de Solicitud", default=date.today(), format="%Y-%m-%d"
    )


class ModificarSolicitudProduccionForm(Form):

    tandas = IntegerField(
        "Número de Tandas",
        [
            validators.DataRequired(message="Ingresa el número de tandas"),
            validators.NumberRange(
                min=1, message="El número de tandas debe ser mayor a 0"
            ),
        ],
    )
    fecha_solicitud = DateField(
        "Fecha de Solicitud", default=date.today(), format="%Y-%m-%d"
    )
    mensaje = TextAreaField("Mensaje")


class BusquedaLoteGalletaForm(Form):
    fecha_inicio = DateField(
        "Fecha de Inicio", format="%Y-%m-%d", validators=[validators.DataRequired()]
    )
    fecha_fin = DateField(
        "Fecha de Fin", format="%Y-%m-%d", validators=[validators.DataRequired()]
    )

    # Assuming get_recetas() returns a list of tuples like [(id, name), ...]
    receta = SelectField("Receta", choices=[], validators=[validators.DataRequired()])


class MermaGalletaForm(Form):
    lot_id = HiddenField("Lot ID")
    tipo_medida = SelectField(
        "Tipo de Medida",
        choices=[("g", "Gramos"), ("p", "Piezas")],
        validators=[validators.DataRequired()],
    )
    cantidad = IntegerField(
        "Cantidad",
        validators=[
            validators.DataRequired(),
            validators.NumberRange(min=1, message="La cantidad debe ser mayor a 0"),
        ],
    )


class MermaInsumoForm(Form):
    lot_id = HiddenField("Lot ID")
    cantidad = IntegerField(
        "Cantidad",
        validators=[
            validators.DataRequired(),
            validators.NumberRange(min=1, message="La cantidad debe ser mayor a 0"),
        ],
    )


class BusquedaCompra(Form):
    fecha_inicio = DateField(
        "Fecha de Inicio", format="%Y-%m-%d", validators=[validators.DataRequired()]
    )
    fecha_fin = DateField(
        "Fecha de Fin", format="%Y-%m-%d", validators=[validators.DataRequired()]
    )

    insumo = SelectField("Insumo", choices=[], validators=[validators.DataRequired()])


class LoteInsumoForm(Form):
    insumos = SelectField("Insumo", choices=[], validators=[validators.DataRequired()])
    cantidad = IntegerField("Cantidad", validators=[validators.DataRequired()])
    fecha_caducidad = DateField(
        "Fecha de Caducidad", format="%Y-%m-%d", validators=[validators.DataRequired()]
    )
    costo_lote = FloatField("Costo del Lote", validators=[validators.DataRequired()])


class NuevaCompraForm(Form):
    proveedores = SelectField(
        "Proveedor", choices=[], validators=[validators.DataRequired()]
    )
    caja = BooleanField("¿Retirar dinero de la caja?", default=True)
    lotes_insumos = FieldList(FormField(LoteInsumoForm), min_entries=1)
