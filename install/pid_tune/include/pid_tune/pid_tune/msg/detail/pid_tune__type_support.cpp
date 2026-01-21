// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from pid_tune:msg/PidTune.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "pid_tune/msg/detail/pid_tune__functions.h"
#include "pid_tune/msg/detail/pid_tune__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace pid_tune
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void PidTune_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) pid_tune::msg::PidTune(_init);
}

void PidTune_fini_function(void * message_memory)
{
  auto typed_message = static_cast<pid_tune::msg::PidTune *>(message_memory);
  typed_message->~PidTune();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember PidTune_message_member_array[3] = {
  {
    "kp",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pid_tune::msg::PidTune, kp),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "ki",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pid_tune::msg::PidTune, ki),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "kd",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pid_tune::msg::PidTune, kd),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers PidTune_message_members = {
  "pid_tune::msg",  // message namespace
  "PidTune",  // message name
  3,  // number of fields
  sizeof(pid_tune::msg::PidTune),
  false,  // has_any_key_member_
  PidTune_message_member_array,  // message members
  PidTune_init_function,  // function to initialize message memory (memory has to be allocated)
  PidTune_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t PidTune_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &PidTune_message_members,
  get_message_typesupport_handle_function,
  &pid_tune__msg__PidTune__get_type_hash,
  &pid_tune__msg__PidTune__get_type_description,
  &pid_tune__msg__PidTune__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace pid_tune


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<pid_tune::msg::PidTune>()
{
  return &::pid_tune::msg::rosidl_typesupport_introspection_cpp::PidTune_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, pid_tune, msg, PidTune)() {
  return &::pid_tune::msg::rosidl_typesupport_introspection_cpp::PidTune_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
