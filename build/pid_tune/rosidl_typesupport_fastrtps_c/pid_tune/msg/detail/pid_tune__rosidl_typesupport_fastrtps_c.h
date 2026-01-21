// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from pid_tune:msg/PidTune.idl
// generated code does not contain a copyright notice
#ifndef PID_TUNE__MSG__DETAIL__PID_TUNE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define PID_TUNE__MSG__DETAIL__PID_TUNE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "pid_tune/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "pid_tune/msg/detail/pid_tune__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
bool cdr_serialize_pid_tune__msg__PidTune(
  const pid_tune__msg__PidTune * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
bool cdr_deserialize_pid_tune__msg__PidTune(
  eprosima::fastcdr::Cdr &,
  pid_tune__msg__PidTune * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
size_t get_serialized_size_pid_tune__msg__PidTune(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
size_t max_serialized_size_pid_tune__msg__PidTune(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
bool cdr_serialize_key_pid_tune__msg__PidTune(
  const pid_tune__msg__PidTune * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
size_t get_serialized_size_key_pid_tune__msg__PidTune(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
size_t max_serialized_size_key_pid_tune__msg__PidTune(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, pid_tune, msg, PidTune)();

#ifdef __cplusplus
}
#endif

#endif  // PID_TUNE__MSG__DETAIL__PID_TUNE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
