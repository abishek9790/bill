from django.db import models

# Create your models here.







def from_1():
    l=material.objects.all().order_by('material_code').last()
    if not l:
        return 1
    return l.material_code+1




class material(models.Model):
    material_type=(('Material','Material'),('Other','Other'))
    item_type=(('Gold','Gold'),('Silver','Silver'),('Diamond','Diamond'))
    hsn_code=(('7113','7113'),('7114','7114'),('7115','7115'))
    units=(('GMS','GMS'),('GMA','GMA'))




    material_code=models.IntegerField(primary_key=True,default=from_1)
    material_type=models.CharField(max_length=100,choices=material_type)
    item_type=models.CharField(max_length=100,choices=item_type)
    material_name=models.CharField(max_length=100)
    purity_perc=models.IntegerField()
    hsn_code=models.CharField(max_length=100,choices=hsn_code)
    purchase_rate=models.IntegerField()
    units=models.CharField(max_length=100,choices=units)
    selling_price=models.IntegerField()
    open_gtm_grs_wt=models.IntegerField()
    current_gtm_grs_wt=models.IntegerField()
    location=models.CharField(max_length=100)
    wastage=models.CharField(max_length=100)

    def __str__(self):
        return self.material_type

class party(models.Model):

    party_turnover=(('10cr','10cr'),('20cr','20cr'),('30cr','30cr'),('40cr','40cr'))



    party_code=models.IntegerField(primary_key=True)
    party_type=models.CharField(max_length=100)
    party_turnover=models.CharField(max_length=100,choices=party_turnover)
    party_name=models.CharField(max_length=100,null=True)
    sub_type=models.CharField(max_length=100)
    debit=models.IntegerField()
    credit=models.IntegerField()
    door_no_street=models.CharField(max_length=100)
    area_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField(max_length=6)
    phone=models.IntegerField(max_length=100)
    mobile=models.IntegerField(max_length=100)
    tin_no=models.IntegerField()
    email=models.CharField(max_length=100)
    state_name=models.CharField(max_length=100)
    hmc_no=models.CharField(max_length=100)
    pan_no=models.CharField(max_length=100)
    state_code=models.IntegerField()
    gstin=models.IntegerField()
    current_balance=models.IntegerField()
    delivery_address=models.CharField(max_length=100)


    def __str__(self):
        return self.party_type


class hsn(models.Model):
    hsn_code1=models.IntegerField(primary_key=True)
    sgst_per=models.IntegerField()
    cgst_per=models.IntegerField()
    igst_per=models.IntegerField()


class invoice(models.Model):
    pay_type=(('RTGS','RTGS'),('RTMA','RTMA'))
    gst_type=(('SGST','SGST'),('SGSA','SGSA'))
    printing_type=(('A4','A4'),('A3','A3'))




    bill_no=models.CharField(max_length=100,primary_key=True)
    order_no=models.IntegerField(unique=True)
    bill_date=models.DateField()
    order_date=models.DateField()
    balance=models.IntegerField()
    turn_over=models.IntegerField()
    name=models.CharField(max_length=100)
    pay_type=models.CharField(max_length=100,choices=pay_type)
    gst_type=models.CharField(max_length=100,choices=gst_type)
    stock=models.IntegerField()
    order_no1=models.IntegerField()
    item_name=models.CharField(max_length=100)
    pcs=models.IntegerField()
    bill_wt=models.IntegerField()
    purity=models.IntegerField()
    rate_grm=models.IntegerField()
    total_rate=models.IntegerField()
    hsn_code2=models.ForeignKey(hsn, on_delete=models.CASCADE)
    jewel_wt=models.IntegerField()
    st_wt=models.IntegerField()
    new_wt=models.IntegerField()
    total_wt=models.IntegerField()
    tcs=models.IntegerField()
    remarks=models.CharField(max_length=100)
    cgst1=models.IntegerField()
    r_off=models.IntegerField()
    r_off=models.IntegerField()
    printing_type=models.CharField(max_length=100,choices=printing_type)
    sgst=models.IntegerField()
    igst=models.IntegerField()
    total=models.IntegerField()


    def __str__(self):
        return self.bill_no