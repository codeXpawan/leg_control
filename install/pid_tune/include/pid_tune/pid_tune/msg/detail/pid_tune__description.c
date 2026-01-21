// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from pid_tune:msg/PidTune.idl
// generated code does not contain a copyright notice

#include "pid_tune/msg/detail/pid_tune__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_pid_tune
const rosidl_type_hash_t *
pid_tune__msg__PidTune__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x1b, 0xe2, 0xe7, 0xfa, 0xe5, 0x4c, 0x51, 0x5b,
      0xa1, 0xe9, 0xc1, 0x4d, 0xd2, 0x72, 0x69, 0xbf,
      0x21, 0xce, 0xdf, 0xa2, 0xac, 0xe3, 0x31, 0x22,
      0xcc, 0xbe, 0x3d, 0xdf, 0xd0, 0xeb, 0x06, 0xe5,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char pid_tune__msg__PidTune__TYPE_NAME[] = "pid_tune/msg/PidTune";

// Define type names, field names, and default values
static char pid_tune__msg__PidTune__FIELD_NAME__kp[] = "kp";
static char pid_tune__msg__PidTune__FIELD_NAME__ki[] = "ki";
static char pid_tune__msg__PidTune__FIELD_NAME__kd[] = "kd";

static rosidl_runtime_c__type_description__Field pid_tune__msg__PidTune__FIELDS[] = {
  {
    {pid_tune__msg__PidTune__FIELD_NAME__kp, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {pid_tune__msg__PidTune__FIELD_NAME__ki, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {pid_tune__msg__PidTune__FIELD_NAME__kd, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
pid_tune__msg__PidTune__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {pid_tune__msg__PidTune__TYPE_NAME, 20, 20},
      {pid_tune__msg__PidTune__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 kp\n"
  "float64 ki\n"
  "float64 kd";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
pid_tune__msg__PidTune__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {pid_tune__msg__PidTune__TYPE_NAME, 20, 20},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 33, 33},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
pid_tune__msg__PidTune__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *pid_tune__msg__PidTune__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
