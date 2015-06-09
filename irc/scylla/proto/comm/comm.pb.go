// Code generated by protoc-gen-go.
// source: comm.proto
// DO NOT EDIT!

/*
Package comm is a generated protocol buffer package.

It is generated from these files:
	comm.proto

It has these top-level messages:
	Metadata
	Event
	Action
	Send
	Response
*/
package comm

import proto "github.com/golang/protobuf/proto"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = math.Inf

// Flags is an enum representing bitflags for messages.
type Flags int32

const (
	Flags_None      Flags = 0
	Flags_OpMod     Flags = 1
	Flags_Broadcast Flags = 2
	Flags_Override  Flags = 3
)

var Flags_name = map[int32]string{
	0: "None",
	1: "OpMod",
	2: "Broadcast",
	3: "Override",
}
var Flags_value = map[string]int32{
	"None":      0,
	"OpMod":     1,
	"Broadcast": 2,
	"Override":  3,
}

func (x Flags) Enum() *Flags {
	p := new(Flags)
	*p = x
	return p
}
func (x Flags) String() string {
	return proto.EnumName(Flags_name, int32(x))
}
func (x *Flags) UnmarshalJSON(data []byte) error {
	value, err := proto.UnmarshalJSONEnum(Flags_value, data, "Flags")
	if err != nil {
		return err
	}
	*x = Flags(value)
	return nil
}

type Action_Condition int32

const (
	Action_OpMod    Action_Condition = 1
	Action_ToOpers  Action_Condition = 2
	Action_Everyone Action_Condition = 3
)

var Action_Condition_name = map[int32]string{
	1: "OpMod",
	2: "ToOpers",
	3: "Everyone",
}
var Action_Condition_value = map[string]int32{
	"OpMod":    1,
	"ToOpers":  2,
	"Everyone": 3,
}

func (x Action_Condition) Enum() *Action_Condition {
	p := new(Action_Condition)
	*p = x
	return p
}
func (x Action_Condition) String() string {
	return proto.EnumName(Action_Condition_name, int32(x))
}
func (x *Action_Condition) UnmarshalJSON(data []byte) error {
	value, err := proto.UnmarshalJSONEnum(Action_Condition_value, data, "Action_Condition")
	if err != nil {
		return err
	}
	*x = Action_Condition(value)
	return nil
}

// Metadata is a key->value pair for message tags.
type Metadata struct {
	Key              *string `protobuf:"bytes,1,req,name=key" json:"key,omitempty"`
	Value            *string `protobuf:"bytes,2,req,name=value" json:"value,omitempty"`
	XXX_unrecognized []byte  `json:"-"`
}

func (m *Metadata) Reset()         { *m = Metadata{} }
func (m *Metadata) String() string { return proto.CompactTextString(m) }
func (*Metadata) ProtoMessage()    {}

func (m *Metadata) GetKey() string {
	if m != nil && m.Key != nil {
		return *m.Key
	}
	return ""
}

func (m *Metadata) GetValue() string {
	if m != nil && m.Value != nil {
		return *m.Value
	}
	return ""
}

// Event represents an incoming event.
type Event struct {
	Source           *string     `protobuf:"bytes,1,req,name=source" json:"source,omitempty"`
	Verb             *string     `protobuf:"bytes,2,req,name=verb" json:"verb,omitempty"`
	Arguments        []string    `protobuf:"bytes,3,rep,name=arguments" json:"arguments,omitempty"`
	Tags             []*Metadata `protobuf:"bytes,4,rep,name=tags" json:"tags,omitempty"`
	Flags            []Flags     `protobuf:"varint,5,rep,name=flags,enum=comm.Flags" json:"flags,omitempty"`
	Actions          []*Action   `protobuf:"bytes,6,rep,name=actions" json:"actions,omitempty"`
	XXX_unrecognized []byte      `json:"-"`
}

func (m *Event) Reset()         { *m = Event{} }
func (m *Event) String() string { return proto.CompactTextString(m) }
func (*Event) ProtoMessage()    {}

func (m *Event) GetSource() string {
	if m != nil && m.Source != nil {
		return *m.Source
	}
	return ""
}

func (m *Event) GetVerb() string {
	if m != nil && m.Verb != nil {
		return *m.Verb
	}
	return ""
}

func (m *Event) GetArguments() []string {
	if m != nil {
		return m.Arguments
	}
	return nil
}

func (m *Event) GetTags() []*Metadata {
	if m != nil {
		return m.Tags
	}
	return nil
}

func (m *Event) GetFlags() []Flags {
	if m != nil {
		return m.Flags
	}
	return nil
}

func (m *Event) GetActions() []*Action {
	if m != nil {
		return m.Actions
	}
	return nil
}

// Action represents an outgoing action.
type Action struct {
	Clientuuid       *string           `protobuf:"bytes,1,req,name=clientuuid" json:"clientuuid,omitempty"`
	Source           *string           `protobuf:"bytes,2,req,name=source" json:"source,omitempty"`
	Target           *string           `protobuf:"bytes,3,req,name=target" json:"target,omitempty"`
	Condition        *Action_Condition `protobuf:"varint,4,opt,name=condition,enum=comm.Action_Condition" json:"condition,omitempty"`
	Verb             *string           `protobuf:"bytes,5,req,name=verb" json:"verb,omitempty"`
	Arguments        []string          `protobuf:"bytes,6,rep,name=arguments" json:"arguments,omitempty"`
	Tags             []*Metadata       `protobuf:"bytes,7,rep,name=tags" json:"tags,omitempty"`
	Broadcast        *bool             `protobuf:"varint,8,opt,name=broadcast" json:"broadcast,omitempty"`
	XXX_unrecognized []byte            `json:"-"`
}

func (m *Action) Reset()         { *m = Action{} }
func (m *Action) String() string { return proto.CompactTextString(m) }
func (*Action) ProtoMessage()    {}

func (m *Action) GetClientuuid() string {
	if m != nil && m.Clientuuid != nil {
		return *m.Clientuuid
	}
	return ""
}

func (m *Action) GetSource() string {
	if m != nil && m.Source != nil {
		return *m.Source
	}
	return ""
}

func (m *Action) GetTarget() string {
	if m != nil && m.Target != nil {
		return *m.Target
	}
	return ""
}

func (m *Action) GetCondition() Action_Condition {
	if m != nil && m.Condition != nil {
		return *m.Condition
	}
	return Action_OpMod
}

func (m *Action) GetVerb() string {
	if m != nil && m.Verb != nil {
		return *m.Verb
	}
	return ""
}

func (m *Action) GetArguments() []string {
	if m != nil {
		return m.Arguments
	}
	return nil
}

func (m *Action) GetTags() []*Metadata {
	if m != nil {
		return m.Tags
	}
	return nil
}

func (m *Action) GetBroadcast() bool {
	if m != nil && m.Broadcast != nil {
		return *m.Broadcast
	}
	return false
}

// Send represents an event being sent to the core.
type Send struct {
	Uuid             *string   `protobuf:"bytes,1,req,name=uuid" json:"uuid,omitempty"`
	Action           []*Action `protobuf:"bytes,2,rep,name=action" json:"action,omitempty"`
	XXX_unrecognized []byte    `json:"-"`
}

func (m *Send) Reset()         { *m = Send{} }
func (m *Send) String() string { return proto.CompactTextString(m) }
func (*Send) ProtoMessage()    {}

func (m *Send) GetUuid() string {
	if m != nil && m.Uuid != nil {
		return *m.Uuid
	}
	return ""
}

func (m *Send) GetAction() []*Action {
	if m != nil {
		return m.Action
	}
	return nil
}

// Response is the response from a policy server when it recieves an event.
type Response struct {
	Continue         *bool     `protobuf:"varint,1,req,name=continue" json:"continue,omitempty"`
	Actions          []*Action `protobuf:"bytes,2,rep,name=actions" json:"actions,omitempty"`
	XXX_unrecognized []byte    `json:"-"`
}

func (m *Response) Reset()         { *m = Response{} }
func (m *Response) String() string { return proto.CompactTextString(m) }
func (*Response) ProtoMessage()    {}

func (m *Response) GetContinue() bool {
	if m != nil && m.Continue != nil {
		return *m.Continue
	}
	return false
}

func (m *Response) GetActions() []*Action {
	if m != nil {
		return m.Actions
	}
	return nil
}

func init() {
	proto.RegisterEnum("comm.Flags", Flags_name, Flags_value)
	proto.RegisterEnum("comm.Action_Condition", Action_Condition_name, Action_Condition_value)
}
