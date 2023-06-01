from django import forms
from app.models import *
from django.core.validators import RegexValidator
from django.core import validators





class materialform(forms.ModelForm):
    botcatcher=forms.CharField(max_length=10,widget=forms.HiddenInput(),required=False)
    purity_perc=forms.IntegerField(required=False)
    purchase_rate=forms.IntegerField(required=False)
    selling_price=forms.IntegerField(required=False)
    open_gtm_grs_wt=forms.IntegerField(required=False)
    current_gtm_grs_wt=forms.IntegerField(required=False)
    location=forms.CharField(max_length=100,required=False)
    wastage=forms.CharField(max_length=100,required=False)
    class Meta:
        model=material
        fields='__all__'
        labels={'material_code':'Material Code','Material_type':'Material Type','item_type':'Item Type','material_name':'Material Name',' purity_perc':'Purity Perc %','hsn_code':'HSN CODE','purchase_rate':'Purchase Rate','units':'Units','selling_price':'Selling Price','open_gtm_grs_wt':'Open GTM GRS Wt','current_gtm_grs_wt':'Current GTM GRS Wt','location':'Location','wastage':'Wastage'}


        def clean_botcatcher(self):
            bot=self.cleaned_data['botcatcher']
            if len(bot)>0:
                raise forms.ValidationError("it is not human")




        


class partyform(forms.ModelForm):
    party_type=forms.CharField(max_length=100,required=False)
    sub_type=forms.CharField(max_length=100,required=False)
    debit=forms.IntegerField(required=False)
    credit=forms.IntegerField(required=False)
    state_name=forms.CharField(required=False)
    hmc_no=forms.IntegerField(required=False)
    pan_no=forms.CharField(required=False,max_length=100)
    state_code=forms.IntegerField(required=False)
    gstin=forms.IntegerField(required=False)
    current_balance=forms.IntegerField(required=False)
    delivery_address=forms.CharField(widget=forms.Textarea(attrs={'cols':50,'rows':3}),required=False)
    class Meta:
        model=party
        fields='__all__'
        labels={'party_code':'Party Code','party_type':'Party Type','party_turnover':'Party Turnover','party_name':'Party Name','sub_type':'Sub Type of','debit':'Debit','credit':'Credit','door_no_street':'Door No & Street','area_name':'Area Name','city':'City','pincode':'Pincode','phone':'Phone','mobile':'Mobile','tin_no':'TIN No','email':'Email Id','state_name':'State Name','hmc_no':'HMC No','pan_no':'PAN No','state_code':'State Code','gstin':'GSTIN','current_balance':'Current Balance','delivery_address':'Delivery Address'}


class hsn_form(forms.ModelForm):
    sgst_per=forms.IntegerField(required=False)
    igst_per=forms.IntegerField(required=False)
    class Meta:
        model=hsn
        fields='__all__'
        labels={'hsn_code1':'Hsn Code','sgst_per':'SGST Per','cgst_per':'CGST Per','igst_per':'IGST Per'}



class invoice_form(forms.ModelForm):
    class Meta:
        model=invoice
        fields='__all__'
        labels={'bill_no':'Bill No','order_no':'Order No','bill_data':'Bill Data','order_date':'Order Date','balance':'Balance','turn_over':'Turn Over','name':'Name','pay_type':'Pay Type','gst_type':'GST Type','stock':'Stock','order_no1':'Order No','item_name':'Item Name','pcs':'Pcs','bill_wt':'Bill Wt','purity':'Purity','rate_grm':'Rate GRM','total_rate':'Total Rate','hsn_code2':'HSN Code','jewel_wt':'Jewel Wt','st_wt':'St Wt','new_wt':'New Wt','total_wt':'Total Wt','tds_applicable':'TCS Applicable','tcs':'TCS','remarks':'Remarks','delivery_add':'Delivery Add','csgt1':'CGST %','r_off':'R Off','printing_type':'Printing Type','duplicate':'Duplicate','empty':'Empty','sgst':'SGST','igst':'IGST','total':'Total','tcs_applicable':'TCS Applicable','huid':'HUID'}

