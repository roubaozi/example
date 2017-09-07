from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import STRING,UINT32

class RequestPasswordReset(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.RequestPasswordReset"
	DEFINITION_VERSION="1.0"
	
	FIELDS=[]

class EmailAsk(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.EmailAsk"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("emailask",STRING),
		("id",UINT32)
		]

class EmailAnswer(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.EmailAnswer"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("emailans",STRING),
		("id",UINT32)
		]

class SecurePasswordQuest(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.SecurePasswordQuest"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("secpwdques",STRING),
		("id",UINT32)
		]
		
class SecurePasswordAns(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.SecurePasswordAns"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("secpwdans",STRING),
		("id",UINT32)
		]

class Result(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.Result"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("result",STRING),
		("id",UINT32)
		]

def basicUnitTest():
	packet1=RequestPasswordReset()
	packet1Bytes=packet1.__serialize__()
	packet1a=RequestPasswordReset.Deserialize(packet1Bytes)
	assert packet1==packet1a
	
	packet2=EmailAsk()
	packet2.emailask="what is your email address?"
	packet2.id=1
	packet2Bytes=packet2.__serialize__()
	packet2a=EmailAsk.Deserialize(packet2Bytes)
	assert packet2==packet2a
	
	packet3=EmailAnswer()
	packet3.emailans="xyrao@outlook.com"
	packet3.id=2
	packet3Bytes=packet3.__serialize__()
	packet3a=EmailAnswer.Deserialize(packet3Bytes)
	assert packet3==packet3a
	
	packet4=SecurePasswordQuest()
	packet4.secpwdques="What is your hometown?"
	packet4.id=3
	packet4Bytes=packet4.__serialize__()
	packet4a=SecurePasswordQuest.Deserialize(packet4Bytes)
	assert packet4==packet4a
	
	packet5=SecurePasswordAns()
	packet5.secpwdans="China"
	packet5.id=4
	packet5Bytes=packet5.__serialize__()
	packet5a=SecurePasswordAns.Deserialize(packet5Bytes)
	assert packet5==packet5a
	
	packet6=Result()
	packet6.result="true"
	packet6.id=5
	packet6Bytes=packet6.__serialize__()
	packet6a=Result.Deserialize(packet6Bytes)
	assert packet6==packet6a

	pktBytes=packet1.__serialize__()+packet2.__serialize__()+packet3.__serialize__()+packet4.__serialize__()+packet5.__serialize__()+packet6.__serialize__()
	deserializer=PacketType.Deserializer()
	deserializer.update(pktBytes)
	for packet in deserializer.nextPackets():
		print("got a packet!")
		if packet==packet1:print("It's packet 1!")
		elif packet==packet2:print("It's packet 2!")
		elif packet==packet3:print("It's packet 3!")
		elif packet==packet4:print("It's packet 4!")
		elif packet==packet5:print("It's packet 5!")
		elif packet==packet6:print("It's packet 6!")
	
	#packet7=Result()
	#packet7.result="true"
	#packet7.id=-5
	#packet7Bytes=packet7.__serialize__()
	#packet7a=Result.Deserialize(packet7Bytes)
	#assert packet7==packet7a
	#When trying the code above, the program reports errors becasue it assigns negative value to the UINT(id).
	#And when comment the code above, the program runs correctly.
	
	print ("The result happened")
	
if  __name__=="__main__":
	basicUnitTest()
	
	
	
