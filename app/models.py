from django.db import models
from django.urls import reverse
  
# ======= 縣市 =======
class City(models.Model):
  name = models.CharField(u'城市',max_length=30)

  def __str__(self):
    return self.name

# ======= 鄉鎮 =======
class Township(models.Model):
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  name = models.CharField(u'鄉鎮',max_length=30)
  zip_code = models.CharField(u'郵遞區號',max_length=30)
  district_court = models.CharField(u'地方法院',max_length=30)
  land_office  = models.CharField(u'地政事務所',max_length=30)
  finance_and_tax_bureau = models.CharField(u'財政稅務局',max_length=30)
  police_station = models.CharField(u'警察局',max_length=30)
  irs = models.CharField(u'國稅局',max_length=30)
  home_office = models.CharField(u'戶政事務所',max_length=30)

  def __str__(self):
    return self.name

# ======= Yfcase =======
class Yfcase(models.Model):
  yfcaseCaseNumber=models.CharField(u'案號(*)',max_length=100)
  yfcaseCompany=models.CharField(u'所屬公司',max_length=50,null=True,blank=True)
  yfcaseCity=models.CharField(u'縣市',max_length=50,null=True,blank=True)
  yfcaseTownship=models.CharField(u'鄉鎮區里',max_length=50,null=True,blank=True)
  # yfcaseCity=models.ForeignKey(City,verbose_name = u'縣市',on_delete=models.SET_NULL,null=True)
  # yfcaseTownship=models.ForeignKey(Township,verbose_name = u'鄉鎮區里', on_delete=models.SET_NULL, null=True)
  yfcaseBigSection=models.CharField(u'段號',max_length=10,null=True,blank=True)
  yfcaseSmallSection=models.CharField(u'小段',max_length=10,null=True,blank=True)
  yfcaseVillage=models.CharField(u'村里',max_length=100,null=True,blank=True)
  yfcaseNeighbor=models.CharField(u'鄰',max_length=100,null=True,blank=True)
  yfcaseStreet=models.CharField(u'街路',max_length=100,null=True,blank=True)
  yfcaseSection=models.CharField(u'段',max_length=100,null=True,blank=True)
  yfcaseLane=models.CharField(u'巷',max_length=100,null=True,blank=True)
  yfcaseAlley=models.CharField(u'弄',max_length=100,null=True,blank=True)
  yfcaseNumber=models.CharField(u'號',max_length=100,null=True)
  yfcaseFloor=models.CharField(u'樓(含之幾)',max_length=100,null=True,blank=True)
  yfcaseCaseStatus = models.CharField(u'案件狀態',max_length=10,null=True,blank=True)

  def __str__(self):
    return self.yfcaseCaseNumber
  
class Land(models.Model):
  yfcase=models.ForeignKey(Yfcase,related_name='lands',on_delete=models.CASCADE)
  landNumber=models.CharField(u'地號',max_length=100,null=True)
  landUrl=models.URLField(u'謄本',max_length=200,null=True,blank=True)
  landArea=models.DecimalField(u'地坪(平方公尺)',default=0,max_digits=10,decimal_places=2,null=True,blank=True)
  landHoldingPointPersonal=models.DecimalField(u'個人持分',default=0,max_digits=10,decimal_places=0,null=True,blank=True)
  landHoldingPointAll=models.DecimalField(u'所有持分',default=0,max_digits=10,decimal_places=0,null=True,blank=True)
  landRemark=models.CharField(u'備註',max_length=100,null=True,blank=True)
  landUpdated = models.DateTimeField(u'案件最後更新時間',auto_now=True,auto_now_add=False)
  
  def __str__(self):
    return self.landNumber
  
# ======= Build =======
class Build(models.Model):
  yfcase=models.ForeignKey(Yfcase,related_name='builds',on_delete=models.CASCADE)
  buildNumber=models.CharField(u'建號',max_length=100,null=True)
  buildUrl=models.URLField(u'謄本',max_length=200,null=True,blank=True)
  buildArea=models.DecimalField(u'建坪(平方公尺)',default=0,max_digits=10,decimal_places=2,null=True,blank=True)
  buildHoldingPointPersonal=models.DecimalField(u'個人持分',default=0,max_digits=10,decimal_places=0,null=True,blank=True)
  buildHoldingPointAll=models.DecimalField(u'所有持分',default=0,max_digits=10,decimal_places=0,null=True,blank=True)
  buildTypeUse=models.CharField(u'建物型',max_length=100,null=True,blank=True)
  buildUsePartition=models.CharField(u'使用分區',max_length=100,null=True,blank=True)
  buildRemark=models.CharField(u'備註',max_length=100,null=True,blank=True)
  buildAncillaryBuildingUseBy=models.CharField(u'附屬建物用途',max_length=100,null=True,blank=True)
  buildAncillaryBuildingArea=models.DecimalField(u'附屬建物面積',default=0,max_digits=6,decimal_places=2,null=True,blank=True)

  def __str__(self):
    return self.buildNumber
  
# ======= Person =======
class Person(models.Model):
  yfcase=models.ForeignKey(Yfcase,related_name='people',on_delete=models.CASCADE)
  name=models.CharField(u'姓名',max_length=100,null=True)
  is_Coowner=models.BooleanField(u'共有人一致',default=False)

  def __str__(self):
    return self.name