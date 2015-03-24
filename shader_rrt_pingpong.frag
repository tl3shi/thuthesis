//片段着色器
uniform sampler2DRect  imageSampler;
uniform sampler2DRect  indexSampler;
uniform int curPointCount;
uniform int curPointStart;

layout(packed) uniform Points
{
    //$MAX_POINT_SIZE$编译前会被替换
   vec4 curPoints[$MAX_POINT_SIZE$];
};

void main()
{	
    vec4 normal_t = texture2DRect(imageSampler, gl_TexCoord[0].xy);
    float index_float = texture2DRect(indexSampler, gl_TexCoord[0].xy).w;
    int index = int(index_float);
    vec3 normal = normal_t.xyz;
    float max = normal_t.w;
    
    for(int i = 0; i < curPointCount; i++)
    {
        float t = dot(curPoints[i].bgr, normal); //BRGA格式
        if(t > max)
        {
            max = t;
            index = curPointStart + i;
        }
    }
   gl_FragData[0] = vec4(normal, max);
   gl_FragData[1] = vec4(0, 0, 0, index);//index为全局索引
}

