from flask import g 
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class Xraylib_Request(FlaskForm):
    #make select field then put all string fields in as subfields? also change stringfields to integer fields where necessary
    comp = StringField('Compound',validators=[DataRequired()])
    int_z = StringField('Element',validators=[DataRequired(), NumberRange(min=1, max=118)])
    int_z_or_comp = StringField('Element or Compound',validators=[DataRequired()])
    float_q = StringField('Momentum Transfer',validators=[DataRequired()])
    linetype = StringField('Transition',validators=[DataRequired()])    
    shell = StringField('Shell',validators=[DataRequired()])
    energy = StringField('Energy', validators=[DataRequired()])
    theta = StringField('Theta', validators=[DataRequired()])
    phi = StringField('Phi', validators=[DataRequired()])
    density = StringField('Density',validators=[DataRequired()])
    pz = StringField('Electron Momentum Pz',validators=[DataRequired()])
    cktrans = StringField('Cktrans',validators=[DataRequired()])
    nistcomp = StringField('Nist Compound',validators=[DataRequired()])
    augtrans = StringField('Auger Trans',validators=[DataRequired()])
    rad_nuc = StringField('Radio Nuclide',validators=[DataRequired()])
        
class Function_Request(FlaskForm):
    function = SelectField('Select Function', 
        choices=[('AtomicWeight', 'Atomic Weight'), ('ElementDensity', 'Element Density'), ('Rayl_FF', 'Rayleigh Form Factor'), ('LineEnergy','Fluorescence Line Energy'), ('EdgeEnergy','Absorption Edge Energy'), ('RadRate','Radiative Transition Probability'), ('JumpFactor','Jump Ratio'), ('FluorYield','Fluorescence Yield'), ('AugerYield','Auger Yield'), ('AtomicLevelWidth','Atomic Level Width'), ('ElectronConfig','Electronic Configuration'), ('CS_Photo_Partial','Partial Photoionization CS'), ('CS_Total','Total CS'), ('CS_Photo','Photoionization CS'), ('CS_Rayl','Rayleigh CS'), ('CS_Compt','Compton CS'), ('CSb_Total','Total CSb'), ('CSb_Photo','Photoionization CSb'), ('CSb_Rayl','Rayleigh CSb'), ('CSb_Compt','Compton CSb')],
        validators=[DataRequired()])
    #choices(value,label)
    submit = SubmitField('Submit', validators=[DataRequired()])
    #doesn't make a submit button just checks if it has been submitted
      
# set up function to only run the chosen xraylib method, might work better if it is a form
          
class Request_Error():
        comp_error = 'Invalid input: Compound'
        int_z_error = 'Invalid input: Element'
        int_z_or_comp_error = 'Invalid input: '
        float_q_error = 'Invalid input : Momentum Transfer.'
        linetype_error = 'Invalid input: '
        shell_error = 'Invalid input: '
        energy_error = 'Invalid input: '
        theta_error = 'Invalid input: '
        phi_error = 'Invalid input: '
        density_error = 'Invalid input: '
        pz_error = 'Invalid input: '
        cktrans_error = 'Invalid input: '
        nistcomp_error = 'Invalid input: '
        augtrans_error = 'Invalid input: '
        rad_nuc_error = 'Invalid input: '    
        #add in other errors
        error = 'Please enter valid input.'
#then when you need error you do error = request_error.error_name
#might be more efficient doing an % if error.xxxx %?

class Request_Units():
        AtomicWeight_u = 'g/mol'
        ElementDensity_u = 'g/cm^3'
        
