//顶点着色器
layout(location = 0) in vec3 inPosition;
flat out vec4 result;
uniform vec4 normal; //xyz：坐标值，w：法向索引
uniform float length;
uniform int normal_count;

void main()
{
    float distance = dot(inPosition, normal.xyz);
    float depth = distance / length; //放缩到 [-1, 1]
    depth = depth * 0.5 + 0.5; //映射到 [0,1]
    vec2 coord = vec2(-1 + normal.w * 2.0 / normal_count, 0.5);
    gl_Position = vec4(coord, depth, 1.0);
    result = vec4(gl_VertexID, 0, 0, 0);
}

//片段着色器
flat in vec4 result;
out vec4 output;

void main()
{
    output = vec4(result.x, 0, 0, 0);
}


