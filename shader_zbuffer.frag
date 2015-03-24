//片段着色器
flat in vec4 result;
out vec4 output;

void main()
{
    output = vec4(result.x, 0, 0, 0);
}

