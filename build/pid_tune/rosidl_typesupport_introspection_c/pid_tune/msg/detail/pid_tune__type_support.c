// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from pid_tune:msg/PidTune.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "pid_tune/msg/detail/pid_tune__rosidl_typesupport_introspection_c.h"
#include "pid_tune/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "pid_tune/msg/detail/pid_tune__functions.h"
#include "pid_tune/msg/detail/pid_tune__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pid_tune__msg__PidTune__init(message_memory);
}

void pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_fini_function(void * message_memory)
{
  pid_tune__msg__PidTune__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_message_member_array[3] = {
  {
    "kp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pid_tune__msg__PidTune, kp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ki",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pid_tune__msg__PidTune, ki),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "kd",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pid_tune__msg__PidTune, kd),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_message_members = {
  "pid_tune__msg",  // message namespace
  "PidTune",  // message name
  3,  // number of fields
  sizeof(pid_tune__msg__PidTune),
  false,  // has_any_key_member_
  pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_message_member_array,  // message members
  pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_init_function,  // function to initialize message memory (memory has to be allocated)
  pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_message_type_support_handle = {
  0,
  &pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_message_members,
  get_message_typesupport_handle_function,
  &pid_tune__msg__PidTune__get_type_hash,
  &pid_tune__msg__PidTune__get_type_description,
  &pid_tune__msg__PidTune__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pid_tune
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pid_tune, msg, PidTune)() {
  if (!pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_message_type_support_handle.typesupport_identifier) {
    pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pid_tune__msg__PidTune__rosidl_typesupport_introspection_c__PidTune_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
