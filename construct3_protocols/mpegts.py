from construct3 import *
'''
transport_packet(){
 sync_byte  8 bslbf
 transport_error_indicator 1 bslbf
 payload_unit_start_indicator 1 bslbf
 transport_priority 1 bslbf
 PID  13 uimsbf
 transport_scrambling_control 2 bslbf
 adaptation_field_control 2 bslbf
 continuity_counter 4 uimsbf
 if(adaptation_field_control == '10' || adaptation_field_control == '11'){
  adaptation_field()
 }
 if(adaptation_field_control == '01' || adaptation_field_control == '11') {
  for (i = 0; i < N; i++){
   data_byte 8 bslbf
    }
 }
}
'''
transport_packet = Struct(
    "sync_byte" / uint8,
    Embedded(BitStruct(
        "transport_error_indicator" / flag,
        "payload_unit_start_indicator" / flag,
        "transport_priority" / flag,
        "PID" / Bits(13),
        "transport_scrambling_control" / Bits(2),
        "adaptation_field_exist" / flag,
        "payload_exist" / flag,
        "continuity_counter" / Bits(4),
        )
    ),
    #'''
    #If(lambda ctx: ctx.adaptation_field_exist,
    #
    #),
    #If(lambda ctx: ctx.payload_exist,
    #
    #),
    #'''
)

if __name__ == "__main__":
    import binascii
    print transport_packet.unpack(binascii.unhexlify("47666666"))

