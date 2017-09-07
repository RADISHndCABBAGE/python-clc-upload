# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
import re



Base = declarative_base()
flag = ""


#解决编码问题。
engine = create_engine('mysql+pymysql://root:newcger@localhost:3306/clc',connect_args={'charset':'utf8'})
metadata = MetaData(engine)
clc = Table('clc',metadata,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('description',String(200)),
    Column('primary_index',String(5)),
    Column('secondary_index_start',String(5)),
    Column('secondary_index_end',String(5)),
    Column('third_index',String(5)))
metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Clc(Base):
    __tablename__ = "clc"
    id = Column(Integer,primary_key=True)
    description = Column(String(200))
    primary_index = Column(String(5))
    secondary_index_start = Column(String(5))
    secondary_index_end = Column(String(5))
    third_index = Column(String(5))



try:
    f = open('/Users/admin/Desktop/CLC.txt','r')
    str = f.readline().strip()
    while(str!=''):

        pattern1 = re.compile("[A-Z0-9/]")
        clcitem = pattern1.findall(str)
        pattern2 = re.compile(u"[\u4e00-\u9fa5、]+")
        clcitem.extend(pattern2.findall(str))
        clc = Clc()
        clc.description = clcitem.pop();

        if(len(clcitem)==1):
            clc.primary_index=clcitem[0]
        elif(len(clcitem)==2):
            global flag
            flag = clcitem[1]
            clc.primary_index=clcitem[0]
            clc.secondary_index_start=clcitem[1]
        elif(len(clcitem)==3 and flag==clcitem[1]):
            clc.primary_index=clcitem[0]
            clc.secondary_index_start=clcitem[1]
            clc.third_index = clcitem[2]
        elif(len(clcitem)==3 and flag!=clcitem[1]):
            clc.primary_index=clcitem[0]
            clc.secondary_index_start=clcitem[1]+clcitem[2]
        elif(len(clcitem)==4):
            clc.primary_index=clcitem[0]
            clc.secondary_index_start = clcitem[1]
            clc.secondary_index_end = clcitem[3]
        else:
            clc.primary_index=clcitem[0]
            clc.secondary_index_start=clcitem[1]+clcitem[2]
            clc.secondary_index_end=clcitem[1]+clcitem[4]
        session.add(clc)
        str = f.readline().strip()

finally:
    if f:
        f.close()
session.commit()
session.close()